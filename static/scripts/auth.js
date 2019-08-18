let auth = true;
$(document)
    .on('click', '.change', function () {
        $(this).addClass('checked').siblings().removeClass('checked');
        if (auth) {
            $('.auth').css('display', 'none');
            $('.reg').css('display', 'block');
            auth = false;
        } else {
            $('.reg').css('display', 'none');
            $('.auth').css('display', 'block');
            auth = true;
        }
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
                .then((data) => console.log(data.status))
                .catch((error) => console.log(error));
        } else {
            if (data['password'] !== data['confirm_password']) {
                alert('Passwords do not match');
            } else {
                delete data['confirm_password'];
                fetch('/req/reg', {
                method: 'POST',
                body: JSON.stringify(data),
            }).then((response) => response.json())
                .then((data) => console.log(data.status))
                .catch((error) => console.log(error));
        }
            }
    });