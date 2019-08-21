// CUSTOM SLIDERS
$.extend( $.ui.slider.prototype.options, { 
    animate: 300
});

$(".slider")
    .slider({
        max: 10,
        min: 1,
        range: "min",
        value: 1,
        orientation: "vertical",
        slide: function( event, ui ) {},
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
}

$(".slider").on("slide", function(event, ui)
{
    let evalValue = ui.value;
    let evalParameterName = $(this).attr("class").split(" ")[1];
    $(this).siblings("p").text(evalValue);
    userEvaluations[evalParameterName] = evalValue;
});

$(".member").on("click", function()
{
    $(this).addClass("opened_member").siblings().removeClass("opened_member");
    changeEvalWinState(this);
    lastObj = this;
})

$("#eval_window_close_button").on("click", function()
{
    changeEvalWinState();
})

const send_eval_params = {
    "apppreciated_id": 1,
    "group_id": 1,
    "date": dateNow(),
    "parameters": userEvaluations,
    "comment": ""
};
$("#send_eval_button").on("click", function()
{
    fetch("/req/send_eval/1",
    {
        method: "post",
        body: JSON.stringify(send_eval_params),
    })
    .then(json)
    .then(function (data)
    {  
        console.log('Request succeeded with JSON response', data);  
    })  
    .catch(function (error)
    {  
        console.log('Request failed', error);  
    });
})

function changeEvalWinState(changedObj = null)
{
    if(evalWinState && changedObj == null)
    {
        closeEvalWin();
        $(lastObj).removeClass("opened_member");
        evalWinState = false;
        lastObj = null;
    }
    else if(lastObj == null)
    {
        openEvalWin();
        evalWinState = true;
    }
}

function openEvalWin()
{
    document.getElementById("eval_window").style.width = "86.3vw";
    document.body.style.overflow = "hidden";
    setTimeout(() => {
        $('.slider_container').each(function()
        {
            this.style.display = "flex";
        });
        document.getElementById("send_eval_button").style.fontSize = "24px";
    }, 175);
    document.getElementsByClassName("fa-times")[0].style.fontSize = "initial";
    console.log("opened");
}

function closeEvalWin()
{
    document.getElementById("eval_window").style.width = "0";
    document.body.style.overflow = "initial";
    setTimeout(() => {
        $('.slider_container').each(function()
        {
            this.style.display = "none";
        });
        document.getElementById("send_eval_button").style.fontSize = "0";
    }, 100);
    document.getElementsByClassName("fa-times")[0].style.fontSize = "0";
    console.log("closed");
}

function dateNow()
{
    const date = new Date();
    return [date.getDate(), date.getMonth()+1, date.getFullYear()].join('.');
}