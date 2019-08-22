let groupForm = $("#new_group_form")[0];

$(document).on("click", ".plus__image", function()
{
    // groupForm.style.zIndex = 1;
    // groupForm.style.opacity = 1;
    groupForm.style.top = "15vh";
});

$(document).on('submit', 'form', function (e)
{
    e.preventDefault();
    const newGroupData = {};
    $(this).find('input').each(function () {
        newGroupData[this.name] = $(this).val();
    });
    if(newGroupData["groupName"] != "" && newGroupData["groupAvatar"] != "")
    {
        groupForm.style.top = "-50vh";
        let reader = new FileReader();
        reader.readAsDataURL($('#group_image_form').prop('files')[0]);
        reader.onload = function (e) {
            const arrayBuffer = e.target.result;
            newGroupData.groupAvatar = arrayBuffer;
        };
        fetch("/req/create_group",
        {
            method: "POST",
            body: JSON.stringify(newGroupData),
        })
        .then((response) => response.json())
        .then((data) => console.log(data))
        .catch((error) => console.log(error));
    }
});