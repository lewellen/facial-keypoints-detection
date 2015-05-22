from fileFormats import TrainFormat, TestFormat, IdLookupTableFormat,\
    SubmissionFormat
from baselineApproach import BaselineModel
from numpy import mean
from OptimizedModel import OptimizedModel

def generateKaggleSubmission():
    trainFormat = TrainFormat()
    train = trainFormat.deserialize("../data/training.csv", limit=None)

    model = OptimizedModel()
    model.fit(train)
    
    testFormat = IdLookupTableFormat()
    test = testFormat.deserialize("../data/IdLookupTable.csv")
    
    predictions = model.predict(test)
    submissionFormat = SubmissionFormat()
    submissionFormat.serialize("../data/guesses.csv", predictions)

if __name__ == '__main__':
    generateKaggleSubmission()
    
#     trainFormat = TrainFormat()
#     train = trainFormat.deserialize("../data/training.csv", limit=None)
# 
#     for x in train:
#         if "left_eye_center_x" in x:
#             print x["left_eye_center_x"]