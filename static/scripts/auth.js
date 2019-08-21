let auth = true;
$(document)
    .on('click', '.reg_btn', function () {
        $(this).addClass('checked').siblings().removeClass('checked');
        $('.auth').css('display', 'none');
        $('.reg').css('display', 'block');
        auth = false;
    })
    .on('click', '.auth_btn', function () {
        $(this).addClass('checked').siblings().removeClass('checked');
        $('.reg').css('display', 'none');
        $('.auth').css('display', 'block');
        auth = true;
    })
    .on('submit', '.form', function (e) {
        e.preventDefault();
        const data = {};
        $(this).find('input, textarea').each(function () {
            data[this.name] = $(this).val();
        });
        if (auth) {
            fetch('/req/auth', {
                method: 'POST',
                body: JSON.stringify(data),
            }).then((response) => response.json())
                .then((data) => {
                console.log(data);
                    if(data.status === 'Ok') {
                        window.location.replace('/');
                    } else {
                        alert(data.message);
                    }
                })
                .catch((error) => console.log(error));
        } else {
            if (data['password'] !== data['confirm_password']) {
                alert('Passwords do not match');
            } else {
                delete data['confirm_password'];
                $('input[type="radio"]').map(function () {
                    this.checked && (data.sex = this.value)
                });
                const reader = new FileReader();
                reader.onload = function (e) {
                    const arrayBuffer = e.target.result;
                    data.image = arrayBuffer;
                    fetch('/req/reg', {
                        method: 'POST',
                        body: JSON.stringify(data),
                    }).then((response) => response.json())
                        .then((data) => {
                            if(data.status === 'Ok') {
                                window.location.replace('/');
                            } else {
                                alert(data.message);
                            }
                        })
                        .catch((error) => console.log(error));
                };
                reader.readAsDataURL($('#file').prop('files')[0]);
            }
        }
        console.log(data);
    });

