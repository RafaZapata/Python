class AzureOutputDM:
    def __init__(self, data):
        self.data = SystemInfo(**data)

class SystemInfo:
    def __init__(self, area_path, team_project, iteration_path, work_item_type, state, reason,
                 assigned_to, created_date, created_by, changed_date, changed_by, comment_count,
                 title, story_points, state_change_date, activated_date, activated_by, priority,
                 description):
        self.SystemAreaPath = area_path
        self.SystemTeamProject = team_project
        self.SystemIterationPath = iteration_path
        self.SystemWorkItemType = work_item_type
        self.SystemState = state
        self.SystemReason = reason
        self.SystemAssignedTo = AssignedTo(**assigned_to)
        self.SystemCreatedDate = created_date
        self.SystemCreatedBy = CreatedBy(**created_by)
        self.SystemChangedDate = changed_date
        self.SystemChangedBy = ChangedBy(**changed_by)
        self.SystemCommentCount = comment_count
        self.SystemTitle = title
        self.MicrosoftVSTSSchedulingStoryPoints = story_points
        self.MicrosoftVSTSCommonStateChangeDate = state_change_date
        self.MicrosoftVSTSCommonActivatedDate = activated_date
        self.MicrosoftVSTSCommonActivatedBy = ActivatedBy(**activated_by)
        self.MicrosoftVSTSCommonPriority = priority
        self.SystemDescription = description

class UserInformation:
    def __init__(self, displayName, id, uniqueName, descriptor):
        self.display_name = displayName
        self.id = id
        self.unique_name = uniqueName
        self.descriptor = descriptor

class AssignedTo(UserInformation):
     pass

class CreatedBy(UserInformation):
     pass

class ChangedBy(UserInformation):
     pass

class ActivatedBy(UserInformation):
     pass