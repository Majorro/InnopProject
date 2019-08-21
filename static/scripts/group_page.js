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

function changeEvalWinState()
{
    if(evalWinState)
    {
        closeEvalWin();
        evalWinState = false;
    }
    else 
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
            // this.style.height = "60vh";
        });
    }, 175);
    document.getElementById("send_eval_button").style.fontSize = "24px";
    // document.getElementById("send_eval_button").style.height = "initial";
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
            // this.style.height = "0";
        });
    }, 100);
    document.getElementById("send_eval_button").style.fontSize = "0";
    // document.getElementById("send_eval_button").style.height = "0";
    document.getElementsByClassName("fa-times")[0].style.fontSize = "0";
    console.log("closed");
}