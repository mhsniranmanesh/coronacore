from symptoms.constants.symptopmsConstants import QUESTIONS_COUNT
from symptoms.models.responses import UserResponse, UserResponseSet


# def getUserStatusFromQuestionsResponses(User, Responses):
#     if Responses is None:
#         Responses = UserResponse.objects.filter(user=User).lastest
#
#

def create_user_response_dict_from_question_responses(responses):
    response_dict = {}
    for response in responses:
        response_dict[response.question.rank] = response.option.rank
    return response_dict


def get_user_response_dict(user):
    last_response_set = UserResponseSet.objects.filter(user=user).latest('id')
    responses = UserResponse.objects.filter(response_set=last_response_set)
    response_dict = create_user_response_dict_from_question_responses(responses=responses)
    return response_dict
