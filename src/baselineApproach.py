class BaselineModel:
    def fit(self, trainExamples):
        self.expectedValues = {}
        
        for x in trainExamples:
            for (key, value) in x.items():
                if key != "Image":
                    if not key in self.expectedValues:
                        self.expectedValues[key] = (0.0, 0.0)
                    
                    if len(value) > 0:
                        _sum, _count = self.expectedValues[key]
                        try:
                            self.expectedValues[key] = (_sum + float(value), _count + 1)
                        except ValueError:
                            print value
                        
        for key in self.expectedValues.keys():
            _sum, _count = self.expectedValues[key]
            self.expectedValues[key] = _sum / _count

        return self
    
    def predict(self, testExamples):
        keyset = set(self.expectedValues.keys())
        
        for x in testExamples:
            yield self.expectedValues[ x["FeatureName"] ]