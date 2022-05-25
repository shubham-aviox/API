from email.policy import default
import uuid

from sqlalchemy import (TEXT, Boolean, Column, DateTime, Float, ForeignKey,
                        Integer, String, UniqueConstraint, func)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import column_property, relationship
from sqlalchemy.sql.expression import false

from admin_lead_management.models import Base

class LeadSource(Base):
    __tablename__ = "lead_source"

    id = Column(
        name="id", type_=UUID(as_uuid=True),
        primary_key=True, nullable=False, default=uuid.uuid4, unique=True
    )
    name = Column(String(100))

    is_deleted = Column(Boolean, default=False)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime, default=func.now(),
        server_onupdate=func.now()
    )

class Status(Base):
    '''
    '''
    __tablename__ = "status"

    id = Column(
        name="id", type_=UUID(as_uuid=True),
        primary_key=True, nullable=False, default=uuid.uuid4, unique=True
    )
    name = Column(String(100))
    role = Column(String(50), default="admin")

    is_deleted = Column(Boolean, default=False)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime, default=func.now(),
        server_onupdate=func.now()
    )

class Leads(Base):
    '''
    '''
    __tablename__ = "leads"

    id = Column(
        name="id", type_=UUID(as_uuid=True),
        primary_key=True, nullable=False, default=uuid.uuid4, unique=True
    )

    name = Column(String(100))
    contact_number = Column(String(20))
    email = Column(String(100))
    country_id = Column(UUID(as_uuid=True))
    state_id = Column(UUID(as_uuid=True))
    city = Column(String(100))
    status_id = Column(UUID, ForeignKey('status.id', ondelete='CASCADE'))
    lead_source_id = Column(UUID, ForeignKey('lead_source.id', ondelete='CASCADE'))
    distributor_id = Column(UUID(as_uuid=True), nullable=True)
    distributor_name = Column(String)
    customer_number = Column(String(100), nullable=True)
    country_name = Column(String(100))
    state_name = Column(String(100))
    created_by = Column(UUID(as_uuid=True), nullable=True)
    campaign_id = Column(String(100), nullable=True)
    lead_type = Column(String(100))
    notes = Column(String)

    is_deleted = Column(Boolean, default=False)

    interested_products = relationship('InterestedProduct', back_populates='lead')
    assignees = relationship('LeadAssignee', back_populates='lead')

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime, default=func.now(),
        server_onupdate=func.now()
    )

class LeadAssignee(Base):
    '''
    '''
    __tablename__ = "lead_assignees"

    id = Column(
        name="id", type_=UUID(as_uuid=True),
        primary_key=True, nullable=False, default=uuid.uuid4, unique=True
    )

    lead_id = Column(UUID, ForeignKey('leads.id', ondelete='CASCADE'))
    agent_id = Column(UUID(as_uuid=True))
    assigned_by = Column(UUID(as_uuid=True))
    agent_name = Column(String)
    is_deleted = Column(Boolean, default=False)
    
    lead = relationship('Leads', uselist=False, back_populates='assignees')
    
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime, default=func.now(),
        server_onupdate=func.now()
    )

class InterestedProduct(Base):
    '''
    '''
    __tablename__ = "interested_products"

    id = Column(
        name="id", type_=UUID(as_uuid=True),
        primary_key=True, nullable=False, default=uuid.uuid4, unique=True
    )

    lead_id = Column(UUID, ForeignKey('leads.id', ondelete='CASCADE'))
    product_name = Column(String(100))
    recommended_action = Column(String, nullable=True)
    
    lead = relationship('Leads', uselist=False, back_populates='interested_products')

    is_deleted = Column(Boolean, default=False)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime, default=func.now(),
        server_onupdate=func.now()
    )


class LeadStatusHistory(Base):
    '''
    '''
    __tablename__ = "lead_histories"

    id = Column(
        name="id", type_=UUID(as_uuid=True),
        primary_key=True, nullable=False, default=uuid.uuid4, unique=True
    )

    lead_id = Column(UUID, ForeignKey('leads.id', ondelete='CASCADE'))
    status_id = Column(UUID, ForeignKey('status.id', ondelete='CASCADE'))
    
    updated_by = Column(UUID(as_uuid=True))

    updated_at = Column(
        DateTime, default=func.now(),
        server_onupdate=func.now()
    )