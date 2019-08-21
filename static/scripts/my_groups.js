fetch('/get_my_groups/')
    .then((response) => response.json())
    .then((response) => {
        const data = response.data;
        data.map((group) => {
           $('#main_view').append(`
           <div class="group">
                <img class="group_logo_img" src="${group.groupimage}" alt="Group Logo">
                <div class="group_info">
                    <h2 class="group_name">${group.groupname}</h2>
                    <span class="group_members_counter">Участников: ${group.count_members}</span><br>
                    <span class="group_recommendations_counter">Рекомендаций: ${group.count_recommendations}</span>
                </div>
            </div>
           `);
        });
    });