from fileFormats import TrainFormat, TestFormat, IdLookupTableFormat,\
    SubmissionFormat
from baselineApproach import BaselineModel

if __name__ == '__main__':
    trainFormat = TrainFormat()
    train = trainFormat.deserialize("../data/training.csv", limit=None)

    model = BaselineModel()
    model.fit(train)
    
    testFormat = IdLookupTableFormat()
    test = testFormat.deserialize("../data/IdLookupTable.csv")
    
    predictions = model.predict(test)
    
    submissionFormat = SubmissionFormat()
    submissionFormat.serialize("../data/guesses.csv", predictions)