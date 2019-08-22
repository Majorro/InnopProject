// CUSTOM SLIDERS
let groupIdSearch = window.location.pathname;
let groupId = '';
for (let i = 6; i < groupIdSearch.length; i++) {
    groupId += groupIdSearch[i];
}

$.extend($.ui.slider.prototype.options, {
    animate: 300
});

$(".slider")
    .slider({
        max: 10,
        min: 1,
        range: "min",
        value: 1,
        orientation: "vertical",
        slide: function (event, ui) {
        },
    });

$(".slider")
    .slider("pips", {
        first: "pip",
        last: "pip"
    })
    .slider("float");
// CUSTOM SLIDERS END

let evalWinState = false; //false - closed, true - opened
let lastObj = null;
//let topBarState = true;
//let evaluationWindow = document.getElementById("eval_window");
//let sliderElements = document.getElementsByClassName("slider");

// par, joi, res, kin, tru, irr, com, iso
let userEvaluations = {
    "par": 1,
    "joi": 1,
    "res": 1,
    "kin": 1,
    "tru": 1,
    "irr": 1,
    "com": 1,
    "iso": 1
};

$(document).on("slide", ".slider", function (event, ui) {
    let evalValue = ui.value;
    let evalParameterName = $(this).attr("class").split(" ")[1];
    $(this).siblings("p").text(evalValue);
    userEvaluations[evalParameterName] = evalValue;
});
const send_eval_params = {
    "appreciated_id": '',
    "group_id": groupId,
    "date": dateNow(),
    "parameters": userEvaluations,
    "comment": ""
};

$(document).on('click', '.member', function () {
    $(this).addClass("opened_member").siblings().removeClass("opened_member");
    changeEvalWinState(this);
    lastObj = this;
    const uId = $(this).children('.uId').val();
    send_eval_params.appreciated_id = uId;
});

$(document).on("click", "#eval_window_close_button", function () {
    changeEvalWinState();
});

$(document).on("click", "#send_eval_button", function () {
    fetch(`/req/send_eval${groupId}`,
        {
            method: "post",
            body: JSON.stringify(send_eval_params),
        })
        .then((response) => response.json())
        .then(function (data) {
            console.log('Request succeeded with JSON response', data);
        })
        .catch(function (error) {
            console.log('Request failed', error);
        });
    changeEvalWinState();
});

function changeEvalWinState(changedObj = null) {
    if (evalWinState && changedObj == null) {
        closeEvalWin();
        $(lastObj).removeClass("opened_member");
        evalWinState = false;
        lastObj = null;
    } else if (lastObj == null) {
        openEvalWin();
        evalWinState = true;
    }
}

function openEvalWin() {
    document.getElementById("eval_window").style.width = "86.3vw";
    document.body.style.overflow = "hidden";
    setTimeout(() => {
        $('.slider_container').each(function () {
            this.style.display = "flex";
        });
        document.getElementById("send_eval_button").style.fontSize = "24px";
    }, 175);
    document.getElementsByClassName("fa-times")[0].style.fontSize = "initial";
    console.log("opened");
}

function closeEvalWin() {
    document.getElementById("eval_window").style.width = "0";
    document.body.style.overflow = "initial";
    setTimeout(() => {
        $('.slider_container').each(function () {
            this.style.display = "none";
        });
        document.getElementById("send_eval_button").style.fontSize = "0";
    }, 100);
    document.getElementsByClassName("fa-times")[0].style.fontSize = "0";
    console.log("closed");
}

function dateNow() {
    const date = new Date();
    return [date.getDate(), date.getMonth() + 1, date.getFullYear()].join('.');
}

fetch(`/req/get_group_info${groupId}`)
    .then((response) => response.json())
    .then((response) => {
        const data = response.data;
        $('.group_name').text(data.groupname);
        $('.group_members_counter').text(`Участников: ${data.members_counter}`);
        $('.group_logo_img').attr('src', data.groupimage);
        $('.bg_image').css('background', `linear-gradient(
          rgba(0, 0, 0, 0.5),
          rgba(0, 0, 0, 0.5)
        ),
    url("${data.groupimage}")`);
    })
    .catch((error) => console.log(error));

fetch(`/req/get_info_about_users_in_group${groupId}`)
    .then((response) => response.json())
    .then((response) => {
        const data = response.data;
        console.log(data);
        const admin = '<i class="fas fa-cog"></i>';
        data.map((user) => {
            $('.group_members').append(`
                    <div class="member">
                        <input type="hidden" class="uId" value="${user.account_id}">
                        <img class="member_avatar_img" src="${user.image}" alt="Member Avatar">
                        <div class="member_info">
                            <div class="member_group_status">
                                <i class="far fa-user"></i>
                                ${user.is_admin ? admin : ''}
                            </div>
                            <span class="member_fullname">${user.first_name}<br>${user.last_name}</span>
                        </div>
                    </div>
            `);
        });
        $('.group_members').append('<div id="bottom_sidebar_line" class="line"></div>');
    })
    .catch((error) => console.log(error));

fetch(`/req/get_my_recommendations${groupId}`)
    .then((response) => response.json())
    .then((response) => {
        const data = response.data;
        data.map((recommendation) => {
            $('#recommendation_container').append(`
            <div class="recommendation_panel">
                        <h2 class="recommendation_title">${recommendation.title}</h2>
                        <div class="line recommendation_panel_line"></div>
                        <p class="recommendation">${recommendation.text}</p>
                    </div>
            `);
        });
    })
    .catch((error) => console.log(error));
