class AverageCalculator:
    
    def __init__(self, grades, weights ):
        self.grades = grades
        self.weights = weights

    def calculate(self):
        try:
            sum_weighted_grades=0
            sum_weights=0

            for grade_str, weight_str in zip(self.grades, self.weights):
                grade = float(grade_str) if grade_str.strip() else 0.0
                weight = float(weight_str)
                sum_weighted_grades += grade * (weight/100)
                sum_weights += weight


            if sum_weights == 0:
                return "Error: La suma de los porcentajes no puede ser 0"
            if sum_weights > 100:
                return "Error: La suma de los porcentajes no puede ser mayor a 100"

            return f"Promedio: {round(sum_weighted_grades,2)}"

        except ValueError:
            return "Error: Por favor, ingrese valores numéricos válidos para las calificaciones y los pesos."
    def grade_to_Approve(self, target_average=5.97):
        try:
            known_sum = 0
            missing_weights = 0
            missing_index=-1

            for i, (grade_str, weight_str) in enumerate(zip(self.grades, self.weights)):
                weight = float(weight_str)
                if grade_str.strip():
                    known_sum += float(grade_str) * (weight / 100)
                else:
                    
                    if missing_index != -1:
                      return "Error: Solo puede haber una nota faltante"
                    missing_index = i
                    missing_weights += weight 
                    
            if missing_index == -1:
                        return ""
                    
            if missing_weights == 0:
                return "Error: La suma de los porcentajes no puede ser 0"
            
            
                
            required_grade = (target_average - known_sum)*100 / (missing_weights)

            if required_grade > 10:
                return "Es imposible aprobar la materia"
            elif required_grade < 0:
                return "Ya aprobaste la materia"
            else:
                return f"Para aprobar la materia necesitas un {round(required_grade,2)} en la nota faltante"

        except ValueError:
            return "Error: Por favor, ingrese valores numéricos válidos para las calificaciones y los pesos."
