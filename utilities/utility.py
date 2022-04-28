class Calculator:
    @classmethod
    def calculate_percent(cls,percent:int,price:float) -> float:
        answer = 0
        answer = ((100 - percent) * price) / 100
        return answer