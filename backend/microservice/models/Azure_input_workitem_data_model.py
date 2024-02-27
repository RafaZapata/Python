from typing import Any
from jsonschema import validate
import logging

class AssignedTo:
    def __init__(self, data = None):
        if data is not None:
            self.UserSK = data['UserSK']
            self.UserId = data['UserId']
            self.UserName = data['UserName']
            self.UserEmail = data['UserEmail']
        else:
            self.UserSK = ""
            self.UserId = ""
            self.UserName = ""
            self.UserEmail = ""
    
    def to_dict(self):
        return {
            "UserSK" : self.UserSK,
            "UserId" : self.UserId,
            "UserName" : self.UserName,
            "UserEmail": self.UserEmail,
        }

class Project:
    def __init__(self, data = None):
        if data is not None:
            self.ProjectSK = data['ProjectSK']
            self.ProjectId = data['ProjectId']
            self.ProjectName = data['ProjectName']
            self.ProjectVisibility = data['ProjectVisibility']
        else:
            self.ProjectSK = ""
            self.ProjectId = ""
            self.ProjectName = ""
            self.ProjectVisibility = ""

    def to_dict(self):
        return {
            "ProjectSK": self.ProjectSK,
            "ProjectId": self.ProjectId,
            "ProjectName": self.ProjectName,
            "ProjectVisibility": self.ProjectVisibility
        }

class Iteration:
    def __init__(self, data):
        self.IterationName = data['IterationName']
        self.StartDate = data['StartDate']
        self.EndDate = data['EndDate']
        self.IterationSK = data['IterationSK']

    def to_dict(self):
        return {
            "IterationSK": self.IterationSK,
            "IterationName": self.IterationName,
            "StartDate": self.StartDate,
            "EndDate": self.EndDate
        }

class Workitem:
    def __init__(self, data):              
         self.WorkItemId = data['WorkItemId']
         self.WorkItemId = data['WorkItemId']
         self.InProgressDate = data['InProgressDate']
         self.CompletedDate = data['CompletedDate']
         self.LeadTimeDays = data['LeadTimeDays']
         self.CycleTimeDays = data['CycleTimeDays']
         self.InProgressDateSK = data['InProgressDateSK']
         self.CompletedDateSK = data['CompletedDateSK']
         self.AnalyticsUpdatedDate = data['AnalyticsUpdatedDate']
         self.ProjectSK = data['ProjectSK']
         self.WorkItemRevisionSK = data['WorkItemRevisionSK']
         self.AreaSK = data['AreaSK']
         self.IterationSK = data['IterationSK']
         self.AssignedToUserSK = data['AssignedToUserSK']
         self.ChangedByUserSK = data['ChangedByUserSK']
         self.CreatedByUserSK = data['CreatedByUserSK']
         self.ActivatedByUserSK = data['ActivatedByUserSK']
         self.ClosedByUserSK = data['ClosedByUserSK']
         self.ResolvedByUserSK = data['ResolvedByUserSK']
         self.ActivatedDateSK = data['ActivatedDateSK']
         self.ChangedDateSK = data['ChangedDateSK']
         self.ClosedDateSK = data['ClosedDateSK']
         self.CreatedDateSK = data['CreatedDateSK']
         self.ResolvedDateSK = data['ResolvedDateSK']
         self.StateChangeDateSK = data['StateChangeDateSK']
         self.Revision = data['Revision']
         self.Watermark = data['Watermark']
         self.Title = data['Title']
         self.WorkItemType = data['WorkItemType']
         self.ChangedDate = data['ChangedDate']
         self.CreatedDate = data['CreatedDate']
         self.State = data['State']
         self.Reason = data['Reason']
         self.FoundIn = data['FoundIn']
         self.IntegrationBuild = data['IntegrationBuild']
         self.ActivatedDate = data['ActivatedDate']
         self.Activity = data['Activity']
         self.BusinessValue = data['BusinessValue']
         self.ClosedDate = data['ClosedDate']
         self.Issue = data['Issue']
         self.Priority = data['Priority']
         self.Rating = data['Rating']
         self.ResolvedDate = data['ResolvedDate']
         self.ResolvedReason = data['ResolvedReason']
         self.Risk = data['Risk']
         self.Severity = data['Severity']
         self.StackRank = data['StackRank']
         self.TimeCriticality = data['TimeCriticality']
         self.ValueArea = data['ValueArea']
         self.CompletedWork = data['CompletedWork']
         self.DueDate = data['DueDate']
         self.Effort = data['Effort']
         self.FinishDate = data['FinishDate']
         self.OriginalEstimate = data['OriginalEstimate']
         self.RemainingWork = data['RemainingWork']
         self.StartDate = data['StartDate']
         self.StoryPoints = data['StoryPoints']
         self.TargetDate = data['TargetDate']
         self.ParentWorkItemId = data['ParentWorkItemId']
         self.TagNames = data['TagNames']
         self.StateCategory = data['StateCategory']
         self.AutomatedTestId = data['AutomatedTestId']
         self.AutomatedTestName = data['AutomatedTestName']
         self.AutomatedTestStorage = data['AutomatedTestStorage']
         self.AutomatedTestType = data['AutomatedTestType']
         self.AutomationStatus = data['AutomationStatus']
         self.StateChangeDate = data['StateChangeDate']
         self.Count = data['Count']
         self.CommentCount = data['CommentCount']
         self.Microsoft_VSTS_CodeReview_AcceptedBySK = data['Microsoft_VSTS_CodeReview_AcceptedBySK']
         self.Microsoft_VSTS_CodeReview_AcceptedDate = data['Microsoft_VSTS_CodeReview_AcceptedDate']
         self.Microsoft_VSTS_CodeReview_ClosedStatus = data['Microsoft_VSTS_CodeReview_ClosedStatus']
         self.Microsoft_VSTS_CodeReview_ClosedStatusCode = data['Microsoft_VSTS_CodeReview_ClosedStatusCode']
         self.Microsoft_VSTS_CodeReview_ClosingComment = data['Microsoft_VSTS_CodeReview_ClosingComment']
         self.Microsoft_VSTS_CodeReview_Context = data['Microsoft_VSTS_CodeReview_Context']
         self.Microsoft_VSTS_CodeReview_ContextCode = data['Microsoft_VSTS_CodeReview_ContextCode']
         self.Microsoft_VSTS_CodeReview_ContextOwner = data['Microsoft_VSTS_CodeReview_ContextOwner']
         self.Microsoft_VSTS_CodeReview_ContextType = data['Microsoft_VSTS_CodeReview_ContextType']
         self.Microsoft_VSTS_Common_ReviewedBySK = data['Microsoft_VSTS_Common_ReviewedBySK']
         self.Microsoft_VSTS_Common_StateCode = data['Microsoft_VSTS_Common_StateCode']
         self.Microsoft_VSTS_Feedback_ApplicationType = data['Microsoft_VSTS_Feedback_ApplicationType']
         self.Microsoft_VSTS_TCM_TestSuiteType = data['Microsoft_VSTS_TCM_TestSuiteType']
         self.Microsoft_VSTS_TCM_TestSuiteTypeId = data['Microsoft_VSTS_TCM_TestSuiteTypeId']
         self.Iteration = Iteration(data['Iteration'])

         if data['Project'] is not None:
             self.Project = Project(data['Project'])
         else:
             self.Project = Project()

         if data['AssignedTo'] is not None:
             self.AssignedTo = AssignedTo(data['AssignedTo'])
         else:
             self.AssignedTo = AssignedTo()
         
    def to_dict(self):
        return {
            "WorkItemId": str(self.WorkItemId) + "-" + self.ChangedDate,
            "Title": self.Title,
            "WorkItemType": self.WorkItemType,
            "ChangedDate": self.ChangedDate,
            "CreatedDate": self.CreatedDate,
            "StoryPoints" : self.StoryPoints,
            "State": self.State,
            "ProjectSK": self.ProjectSK,
            "WorkItemRevisionSK": self.WorkItemRevisionSK,
            "AreaSK": self.AreaSK,
            "IterationSK": self.IterationSK,
            "AssignedToUserSK": self.AssignedToUserSK,
            "ChangedByUserSK": self.ChangedByUserSK,
            "CreatedByUserSK": self.CreatedByUserSK,
            "ActivatedByUserSK": self.ActivatedByUserSK,
            "ClosedByUserSK": self.ClosedByUserSK,
            "ResolvedByUserSK": self.ResolvedByUserSK,
            "ActivatedDateSK": self.ActivatedDateSK,
            "ChangedDateSK": self.ChangedDateSK,
            "ClosedDateSK": self.ClosedDateSK,
            "CreatedDateSK": self.CreatedDateSK,
            "ResolvedDateSK": self.ResolvedDateSK,
            "StateChangeDateSK": self.StateChangeDateSK,
            "Revision": self.Revision,
            "Reason": self.Reason,
            "Iteration" : [self.Iteration.to_dict()],
            "Project" : [self.Project.to_dict()],
            "AssignedTo" : [self.AssignedTo.to_dict()],
        }

schema_workitems = {
    "type": "object",
    "properties": {
        "@odata.context": {"type": "string"},
        "vsts.warnings@odata.type": {"type": "string"},
        "@vsts.warnings": {"type": "array"},
        "value": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "StoryPoints": {"type": ["number", "null"]},
                    "WorkItemId": {"type": "integer"},
                    "Title": {"type": "string"},
                    "WorkItemType": {"type": "string"},
                    "ChangedDate": {"type": "string", "format": "date-time"},
                    "CreatedDate": {"type": "string", "format": "date-time"},
                    "State": {"type": "string"},
                    "ProjectSK": {"type": "string"},
                    "WorkItemRevisionSK": {"type": "integer"},
                    "AreaSK": {"type": "string"},
                    "IterationSK": {"type": "string"},
                    "AssignedToUserSK": {"type": ["string", "null"]},
                    "ChangedByUserSK": {"type": "string"},
                    "CreatedByUserSK": {"type": "string"},
                    "ActivatedByUserSK": {"type": ["string", "null"]},
                    "ClosedByUserSK": {"type": ["string", "null"]},
                    "ResolvedByUserSK": {"type": ["string", "null"]},
                    "ActivatedDateSK": {"type": ["integer", "null"]},
                    "ChangedDateSK": {"type": "integer"},
                    "ClosedDateSK": {"type": ["integer", "null"]},
                    "CreatedDateSK": {"type": "integer"},
                    "ResolvedDateSK": {"type": ["integer", "null"]},
                    "StateChangeDateSK": {"type": ["integer", "null"]},
                    "Revision": {"type": "integer"},
                    "Reason": {"type": "string"},
                    "Iteration": {
                        "type": "object",
                        "properties": {
                            "IterationName": {"type": "string"},
                            "StartDate": {"type": ["string", "null"]},
                            "EndDate": {"type": ["string", "null"]}
                            },
                        "required": ["IterationName"]
                    },
                    "Project": {
                        "type" : "object",
                        "properties": {
                            "ProjectSK": {"type": "string"},
                            "ProjectId": {"type": "string"},
                            "ProjectName": {"type": "string"},
                            "ProjectVisibility": {"type": "string"},
                        },
                        "required": ["ProjectSK", "ProjectId"]
                    },
                    "AssignedTo": {
                        "type" : ["object", "null"],
                        "properties": {
                            "UserSK": {"type": "string"},
                            "UserId": {"type": "string"},
                            "UserName": {"type": "string"},
                            "UserEmail": {"type": "string"},
                        },
                        "required": ["UserSK", "UserId"]
                    }
                },
                "required": [
                    "WorkItemId",
                    "Title",
                    "WorkItemType",
                    "ChangedDate",
                    "CreatedDate",
                    "State",
                    "ProjectSK",
                    "WorkItemRevisionSK",
                    "AreaSK",
                    "IterationSK",
                    "ChangedByUserSK",
                    "CreatedByUserSK",
                    "ChangedDateSK",
                    "CreatedDateSK",
                    "StateChangeDateSK",
                    "Revision",
                    "Reason",
                ]
            }
        }
    },
    "required": ["@odata.context", "vsts.warnings@odata.type", "@vsts.warnings", "value"]
}

class AzureInputWorkitemDM:
    def __init__(self, json_workitems):
        #self.workitems = [Workitem(**workitem) for workitem in value]
        work_items = []
        for item_data in json_workitems["value"]:
            work_item = Workitem(item_data)
            work_items.append(work_item)

        self.workitems =work_items 
    
    def to_dict(self):
        return {
            "workitems" : [workitem.to_dict() for workitem in self.workitems]
        }

    def validate_schema(json_workitems):
        try:
            validate(instance= json_workitems, schema=schema_workitems)
            return True
        except Exception as e:
            return False