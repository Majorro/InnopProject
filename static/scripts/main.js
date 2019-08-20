fetch('/req/get_user_info')
    .then((response) => response.json())
    .then((response) => {
        const data = response.data;
        $('.bg_image').css('background', `linear-gradient(
          rgba(0, 0, 0, 0.5),
          rgba(0, 0, 0, 0.5)
        ),
    url("${data.image}");`);
        $('.text__login').text(data.login);
        $('.text__MiniInfo').text(`${data.first_name + ' ' + data.last_name}<br>
\t\t                    Дата рождения: ${data.date}`);
        $('.text__description').text(data.person_description);
        (data.sex === 'female') && $('.sex__icon').removeClass('fa-mars').addClass('fa-venus');

    });