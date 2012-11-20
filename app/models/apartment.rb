class Apartment < ActiveRecord::Base
  attr_accessible :address, :city, :zipcode, :content

  belongs_to :user

  validates :user_id, presence: true
  validates :content, presence: true, length: { maximum: 140 }

  default_scope order: 'microposts.created_at DESC'


end
