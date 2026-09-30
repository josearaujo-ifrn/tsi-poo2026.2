 @classmethod
    def de_registro(cls, texto: str) -> "Data":
        no, lo, vali, qua, valo = texto.split(";")
        data = date.fromisoformat(vali)
        return cls( no, lo, data, int(qua), int(valo) )
  @staticmethod
    def dias_para_vencer(data: date):
        hoje = date.today()
        dif = hoje - data
        return dif
