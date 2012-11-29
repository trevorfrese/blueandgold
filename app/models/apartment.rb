class Apartment < ActiveRecord::Base
  attr_accessible :address, :city, :zipcode, :content

  belongs_to :user

  validates :user_id, presence: true
  validates :content, presence: true, length: { maximum: 600 }
  #validates :address, presence: true, length: { maximum: 200 }

  valid_address_regex = //
  #if i can find an address regex that would be great, but its not uniform
  validates :address, :presence => true,
                    :format => { :with => valid_address_regex },
                    :length => { :maximum => 200 }


  default_scope order: 'apartments.created_at DESC'


end
