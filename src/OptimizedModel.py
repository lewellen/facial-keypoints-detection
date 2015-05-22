from scipy.stats.stats import mode

class OptimizedModel:
    def fit(self, trainExamples):
        self.expectedValues = {}
        
        for x in trainExamples:
            for (key, value) in x.items():
                if key != "Image":
                    if not key in self.expectedValues:
                        self.expectedValues[key] = []
                    
                    if len(value) > 0:
                        self.expectedValues[key].append(round(float(value)/0.5,0)*0.5)
                        
        for key in self.expectedValues.keys():
            self.expectedValues[key], _ = mode(self.expectedValues[key])
            self.expectedValues[key] = self.expectedValues[key][0]
            

        return self
    
    def predict(self, testExamples):
        for x in testExamples:
            yield self.expectedValues[ x["FeatureName"] ]