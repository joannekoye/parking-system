from app import ma
from .models import Institution,Lot

class InstitutionSchema(ma.Schema):
    class Meta:
        fields = ('id','name','tag_name','active','quantity')

class LotSchema(ma.Schema):
    class Meta:
        fields =('id','name','user_id_in','session_id_in') 

institutions_schema = InstitutionSchema(many=True)
lot_schema = LotSchema(many=True)
