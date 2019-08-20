def update_user_recommendation(user, posts):
    result_data = user['result_data']
    result_recommendation = dict()
    # Редактирование result data, result_recomendation, posts - это оценкци пользователей

    # posts  [post1, post2, post3]

    # post:
    #     post_id - 4,
    #     author_id - 2,
    #     appreciated_id - 3,
    #     group_id = 4,
    #     date = '2222-01-12', # year, month, day
    #     parameters = {
    #           'par1':1,
    #           'par2':1,
    #           'par2': 2,
    #     }

    for post in posts:
        post['parameters']['par1'] = 1




    user['result_data'] = result_data
    user['result_recommendation'] = {'Стрессоустойчивость': 'Относитесь к вещам с улыбкой',
     'Общение': 'поменьше мата в речи'}

    return user
