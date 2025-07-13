from iacs_api.database import get_db
from geoalchemy2 import Geometry, WKBElement
from iacs_api.database import Base
from sqlalchemy.orm import Mapped, mapped_column


from sqlalchemy import Integer, String, Boolean, Float, UniqueConstraint

class Fields(Base):
    __tablename__ = 'fields'
    
    id: Mapped[int] = mapped_column("id", autoincrement=True, nullable=False, unique=True, primary_key=True, init=False)

    field_id: Mapped[int] = mapped_column(Integer, nullable=False, unique=True)
    farm_id: Mapped[int] = mapped_column(Integer, nullable=True)

    crop_code: Mapped[str] = mapped_column(String, nullable=False)
    crop_name: Mapped[str] = mapped_column(String, nullable=False)
    EC_trans_n: Mapped[str] = mapped_column(String, nullable=False)
    EC_hcat_n: Mapped[str] = mapped_column(String, nullable=False)
    EC_hcat_c: Mapped[str] = mapped_column(String, nullable=False)

    organic: Mapped[bool] = mapped_column(Boolean, nullable=True)
    field_size: Mapped[float] = mapped_column(Float, nullable=False)
    crop_area: Mapped[float] = mapped_column(Float, nullable=True)

    nation: Mapped[str] = mapped_column(String, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)

    geometry: Mapped[WKBElement] = mapped_column(Geometry("POLYGON"), nullable=True)

    __table_args__ = (
        UniqueConstraint('field_id', 'nation', 'year', name='unique_field_year'),
        {'schema': 'iacs'}
    )

    def __init__(self, field_id, crop_code, crop_name, EC_trans_n, EC_hcat_n, EC_hcat_c,
                 field_size, nation, year, farm_id=None, organic=None,
                 crop_area=None, geometry=None):

        self.field_id = field_id
        self.farm_id = farm_id

        self.crop_code = crop_code
        self.crop_name = crop_name
        self.EC_trans_n = EC_trans_n
        self.EC_hcat_n = EC_hcat_n
        self.EC_hcat_c = EC_hcat_c

        self.organic = organic
        self.field_size = field_size
        self.crop_area = crop_area

        self.nation = nation
        self.year = year
        self.geometry = geometry

    def register_if_not_exist(self):
        exists = Fields.query.filter_by(field_id=self.field_id, nation=self.nation, year=self.year).first()
        if not exists:
            Base.session.add(self)
            Base.session.commit()
        return True

    @staticmethod
    def get_by_field_id(field_id, nation, year):
        return Fields.query.filter_by(field_id=field_id, nation=nation, year=year).first()

    def __repr__(self):
        return f"<Fields {self.field_id} ({self.year}) – {self.crop_name}>"