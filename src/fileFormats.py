from csv import DictReader

class TrainFormat:
    def deserialize(self, filePath, limit = None):
        with open(filePath) as handle:
            dictReader = DictReader(handle, delimiter=',', fieldnames=["left_eye_center_x", "left_eye_center_y", "right_eye_center_x", "right_eye_center_y", 
               "left_eye_inner_corner_x", "left_eye_inner_corner_y", "left_eye_outer_corner_x", "left_eye_outer_corner_y", "right_eye_inner_corner_x", 
               "right_eye_inner_corner_y", "right_eye_outer_corner_x", "right_eye_outer_corner_y", "left_eyebrow_inner_end_x", "left_eyebrow_inner_end_y", 
               "left_eyebrow_outer_end_x", "left_eyebrow_outer_end_y", "right_eyebrow_inner_end_x", "right_eyebrow_inner_end_y", "right_eyebrow_outer_end_x", 
               "right_eyebrow_outer_end_y", "nose_tip_x", "nose_tip_y", "mouth_left_corner_x", "mouth_left_corner_y", "mouth_right_corner_x", "mouth_right_corner_y", 
               "mouth_center_top_lip_x", "mouth_center_top_lip_y", "mouth_center_bottom_lip_x", "mouth_center_bottom_lip_y", "Image"])
            
            isFirst = True
            
            for example in dictReader:
                if isFirst:
                    isFirst = False
                    continue
                
                yield example
                
                if limit != None:
                    if limit <= 0:
                        break
                    limit -= 1
                    
class TestFormat:
    def deserialize(self, filePath):
        with open(filePath) as handle:
            dictReader = DictReader(handle, delimiter=',', fieldnames=["ImageId,Image"])
            for example in dictReader:
                yield example

class IdLookupTableFormat:
    def deserialize(self, filePath, limit = None):
        with open(filePath) as handle:
            dictReader = DictReader(handle, delimiter=',', fieldnames=["RowId", "ImageId", "FeatureName"])
            
            isFirst = True
            
            for example in dictReader:
                if isFirst:
                    isFirst = False
                    continue
                
                yield example
                
                if limit != None:
                    if limit <= 0:
                        break
                    limit -= 1

class SubmissionFormat:
    def serialize(self, filePath, Y):
        with open(filePath, 'wb') as handle:
            handle.write("RowId,Location\n")
            handle.writelines(["%d,%s\n" % (i,y) for (i, y) in enumerate(Y, start=1)])