// Copyright 2021 Rapyuta Robotics Co., Ltd.
// This code has been autogenerated from {{data.Filename}} - do not modify

#include "Actions/ROS2{{data.NameCap}}Action.h"

const rosidl_action_type_support_t* UROS2{{data.NameCap}}Action::GetTypeSupport() const
{
    return ROSIDL_GET_ACTION_TYPE_SUPPORT({{data.Group}}, {{data.NameCap}});
}

void UROS2{{data.NameCap}}Action::Init()
{
    Super::Init();
    {{data.Group}}__action__{{data.NameCap}}_SendGoal_Request__init(&{{data.NameCap}}_goal_request);
    {{data.Group}}__action__{{data.NameCap}}_SendGoal_Response__init(&{{data.NameCap}}_goal_response);
    {{data.Group}}__action__{{data.NameCap}}_GetResult_Request__init(&{{data.NameCap}}_result_request);
    {{data.Group}}__action__{{data.NameCap}}_GetResult_Response__init(&{{data.NameCap}}_result_response);
    {{data.Group}}__action__{{data.NameCap}}_FeedbackMessage__init(&{{data.NameCap}}_feedback_message);
}

void UROS2{{data.NameCap}}Action::Fini()
{
    {{data.Group}}__action__{{data.NameCap}}_SendGoal_Request__fini(&{{data.NameCap}}_goal_request);
    {{data.Group}}__action__{{data.NameCap}}_SendGoal_Response__fini(&{{data.NameCap}}_goal_response);
    {{data.Group}}__action__{{data.NameCap}}_GetResult_Request__fini(&{{data.NameCap}}_result_request);
    {{data.Group}}__action__{{data.NameCap}}_GetResult_Response__fini(&{{data.NameCap}}_result_response);
    {{data.Group}}__action__{{data.NameCap}}_FeedbackMessage__fini(&{{data.NameCap}}_feedback_message);
    Super::Fini();
}

void UROS2{{data.NameCap}}Action::SetGoalRequest(const F{{data.StructName}}SendGoalRequest& Goal)
{
    Goal.SetROS2({{data.NameCap}}_goal_request);
}

void UROS2{{data.NameCap}}Action::GetGoalRequest(F{{data.StructName}}SendGoalRequest& Goal) const
{
    Goal.SetFromROS2({{data.NameCap}}_goal_request);
}

void UROS2{{data.NameCap}}Action::SetGoalResponse(const F{{data.StructName}}SendGoalResponse& Goal)
{
    Goal.SetROS2({{data.NameCap}}_goal_response);
}

void UROS2{{data.NameCap}}Action::GetGoalResponse(F{{data.StructName}}SendGoalResponse& Goal) const
{
    Goal.SetFromROS2({{data.NameCap}}_goal_response);
}

void UROS2{{data.NameCap}}Action::SetResultRequest(const F{{data.StructName}}GetResultRequest& Result)
{
    Result.SetROS2({{data.NameCap}}_result_request);
}

void UROS2{{data.NameCap}}Action::GetResultRequest(F{{data.StructName}}GetResultRequest& Result) const
{
    Result.SetFromROS2({{data.NameCap}}_result_request);
}

void UROS2{{data.NameCap}}Action::SetResultResponse(const F{{data.StructName}}GetResultResponse& Result)
{
    Result.SetROS2({{data.NameCap}}_result_response);
}

void UROS2{{data.NameCap}}Action::GetResultResponse(F{{data.StructName}}GetResultResponse& Result) const
{
    Result.SetFromROS2({{data.NameCap}}_result_response);
}


void UROS2{{data.NameCap}}Action::SetFeedback(const F{{data.StructName}}FeedbackMessage& Feedback)
{
    Feedback.SetROS2({{data.NameCap}}_feedback_message);
}

void UROS2{{data.NameCap}}Action::GetFeedback(F{{data.StructName}}FeedbackMessage& Feedback) const
{
    Feedback.SetFromROS2({{data.NameCap}}_feedback_message);
}

void UROS2{{data.NameCap}}Action::SetGoalIdToFeedback(F{{data.StructName}}FeedbackMessage& Feedback)
{
    for (int i = 0; i < 16; i++)
    {
        Feedback.GoalId[i] = {{data.NameCap}}_goal_request.goal_id.uuid[i];
    }
}

void* UROS2{{data.NameCap}}Action::GetGoalRequest()
{
    return &{{data.NameCap}}_goal_request;
}

void* UROS2{{data.NameCap}}Action::GetGoalResponse()
{
    return &{{data.NameCap}}_goal_response;
}

void* UROS2{{data.NameCap}}Action::GetResultRequest()
{
    return &{{data.NameCap}}_result_request;
}

void* UROS2{{data.NameCap}}Action::GetResultResponse()
{
    return &{{data.NameCap}}_result_response;
}

void* UROS2{{data.NameCap}}Action::GetFeedbackMessage()
{
    return &{{data.NameCap}}_feedback_message;
}
