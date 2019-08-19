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
                .then((data) => console.log(data.status))
                .catch((error) => console.log(error));
        } else {
            if (data['password'] !== data['confirm_password']) {
                alert('Passwords do not match');
            } else {
                delete data['confirm_password'];
                $('#toBase64').attr('src', data.image);
                const reader = new FileReader();
                reader.onload = function(e){
                    const arrayBuffer = e.target.result;
                    data.image = arrayBuffer;
                };
                reader.readAsDataURL($('#file').prop('files')[0]);
                console.log($('#file').prop('files')[0]);
                fetch('/req/reg', {
                    method: 'POST',
                    body: JSON.stringify(data),
                }).then((response) => response.json())
                    .then((data) => console.log(data.status))
                    .catch((error) => console.log(error));
            }
        }
        console.log(data);
    });

// document.querySelector('#file').addEventListener('change', function(){
//     var reader = new FileReader();
//     reader.onload = function(){
//         var arrayBuffer = this.result;
//         console.log(arrayBuffer);
//         document.querySelector('#result').innerHTML = arrayBuffer + '  '+arrayBuffer.byteLength;
//     };
//     reader.readAsArrayBuffer(this.files[0]);
// }, false);

// function getBase64Image(img) {
//     // создаем канвас элемент
//     const canvas = document.createElement("canvas");
//     canvas.width = img.width;
//     canvas.height = img.height;
//
//     // Копируем изображение на канвас
//     const ctx = canvas.getContext("2d");
//     ctx.drawImage(img, 0, 0);
//
//     // Получаем data-URL отформатированную строку
//     // Firefox поддерживает PNG и JPEG.
//     const dataURL = canvas.toDataURL("image/png");
//
//     return dataURL.replace(/^data:image\/(png|jpg);base64,/, "");
// }
// function getBase64ImageById(id){
//    return getBase64Image(document.getElementById(id));
// }
