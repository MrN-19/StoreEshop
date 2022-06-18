class Calculator:
    @classmethod
    def calculate_percent(cls,percent:int,price:float) -> float:
        answer = 0
        answer = ((100 - percent) * price) / 100
        return answer
    
class StringModifier:
    @classmethod
    def change_request_path_value(cls,request,new_value):
        request.path = new_value
        return request
