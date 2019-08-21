let evalWinState = false; //false - closed, true - opened
//let topBarState = true;
//let evaluationWindow = document.getElementById("eval_window");

function changeEvalWinState() {
    if (evalWinState) {
        closeEvalWin();
        evalWinState = false;
    } else {
        openEvalWin();
        evalWinState = true;
    }
}

function openEvalWin() {
    document.getElementById("eval_window").style.width = "86.3vw";
    document.body.style.overflow = "hidden";
    document.getElementsByClassName("fa-times")[0].style.fontSize = "initial";
    console.log("opened");
}

function closeEvalWin() {
    document.getElementById("eval_window").style.width = "0";
    document.body.style.overflow = "initial";
    document.getElementsByClassName("fa-times")[0].style.fontSize = "0";
    console.log("closed");
}

let groupId = window.location.pathname;

fetch(`/req/get_group_info${groupId}`)
    .then((response) => response.json())
    .then((response) => {
        const data = response.data;
        $('.group_name').text(data.groupname);
        $('.group_members_counter').text(`Участников: ${data.members_counter}`);
        $('.member_avatar_img').attr('src', data.groupimage);
    })
    .catch((error) => console.log(error));

fetch(`/req/get_my_recommendations${groupId}`)
    .then((response) => response.json())
    .then((response) => {
        const data = response.result_data;
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