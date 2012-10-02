class Apartment < ActiveRecord::Base
  attr_accessible :address, :city, :zipcode

  belongs_to :user
end
