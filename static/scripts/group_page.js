let evalWinState = false; //false - closed, true - opened
//let topBarState = true;
//let evaluationWindow = document.getElementById("eval_window");

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
    document.getElementsByClassName("fa-times")[0].style.fontSize = "initial";
    console.log("opened");
}

function closeEvalWin()
{
    document.getElementById("eval_window").style.width = "0";
    document.body.style.overflow = "initial";
    document.getElementsByClassName("fa-times")[0].style.fontSize = "0";
    console.log("closed");
}