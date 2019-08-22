let groupForm = $("#new_group_form")[0];
let memberForm = $("#new_member_form")[0];
let newGroupName;
let newGroupAvatar;
let gId;
let url;

$(document).on("click", ".plus__image", function()
{
    // groupForm.style.zIndex = 1;
    // groupForm.style.opacity = 1;
    groupForm.style.top = "15vh";
});


$(document).on('submit', '#new_group_form', function (e)
{
    e.preventDefault();
    let newGroupData = {};
    $(this).find('input').each(function () {
        newGroupData[this.name] = $(this).val();
    });
    if(newGroupData["groupname"] != "" && newGroupData["groupimage"] != "")
    {
        groupForm.style.top = "-50vh";
        let reader = new FileReader();
        reader.readAsDataURL($('#group_image_form').prop('files')[0]);
        reader.onload = function (e) {
            const arrayBuffer = e.target.result;
            newGroupData.groupimage = arrayBuffer;
            // $("#last_elem").before(
            //     `<div class="one__group">
            //         <div class="group_padding">
            //             <div class="content__group">
            //                 <div class="top__data">
            //                     <div class="left__panel">
            //                         <div class="group__image" style="background-image: url("${newGroupData.groupimage}");">
                                    
            //                         </div>
            //                     </div>

            //                     <div class="right__panel">
            //                         <div class="group__name">
            //                             ${newGroupData.groupname}
            //                         </div>

            //                         <div class="count__members">
            //                             Участников: 0
            //                         </div>

            //                         <div class="count__recommendations">
            //                             Рекомендаций: 0
            //                         </div>
            //                     </div>
            //                 </div>



            //                 <div class="botton__data">
            //                         <a href="#" class="my__button">Удалить</a>
            //                         <a href="#" class="my__button" id="add_user_button">Добавить пользователя</a>
            //                         <a href="#" class="my__button">Просмотр</a>

            //                 </div>
            //             </div>
            //         </div>
            //     </div>`
            // )
            fetch("/req/create_group",
            {
                method: "POST",
                body: JSON.stringify(newGroupData),
            })
            .then((response) => response.json())
            .then((data) => console.log(data))
            .catch((error) => console.log(error));
        };
    }
});
$(document).on("click", "#add_user_button", function()
{
    memberForm.style.top = "15vh";
    gId = $(this).siblings("#groupId").val();
});

$(document).on('submit', '#new_member_form', function (e)
{
    e.preventDefault();
    let newMemberData = {};
    $(this).find('input').each(function () {
        newMemberData[this.name] = $(this).val();
    });
    login = {login: newMemberData.login}
    if(login != "")
    {
        memberForm.style.top = "-50vh";
        fetch(`/req/add_user_to_group/${gId}`,
        {
            method: "POST",
            body: JSON.stringify(login),
        })
        .then((response) => response.json())
        .then((data) => console.log(data))
        .catch((error) => console.log(error));
    }
});


fetch("/req/get_my_groups")
    .then((response) => response.json())
    .then((data) => 
    {
        let groups = data.data;
        groups.map((groupData) =>
        {
            const watch = '/group/' + groupData.group_id;
            $(".my__groups").prepend(`
            <div class="one__group">
                    <div class="group_padding">
                        <div class="content__group">
                            <div class="top__data">
                                <div class="left__panel">
                                    <img class="group__image" src="${groupData.groupimage}>
                                </div>

                                <div class="right__panel">
                                    <div class="group__name">
                                        ${groupData.groupname}
                                    </div>

                                    <div class="count__members">
                                        Участников: ${groupData.count_members}
                                    </div>

                                    <div class="count__recommendations">
                                        Рекомендаций: ${groupData.count_recommendations}
                                    </div>
                                </div>
                            </div>



                            <div class="botton__data">
                                    <input type="hidden" id="groupId" value="${groupData.group_id}">
                                    <a href="#" class="my__button">Удалить</a>
                                    <a href="#" class="my__button" id="add_user_button">Добавить пользователя</a>
                                    <a href=${watch} class="my__button watch">Просмотр</a>
                            </div>
                        </div>
                    </div>
                </div>
                `)
        });
    })
    .catch((error) => console.log(error))
