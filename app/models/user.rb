class User < ActiveRecord::Base
  attr_accessible :name, :email, :password, :password_confirmation

  has_many :apartments, dependent: :destroy

has_secure_password

valid_email_regex = /\b[A-Z0-9._%a-z\-]+@umail\.ucsb\.edu/

validates_presence_of :name, :password
validates_uniqueness_of :name
validates :password, :presence => { :on => :create }, length: {minimum: 6}
validates :password_confirmation, presence: true
validates :email,   :presence => true,
                    :format => { :with => valid_email_regex },
                    :uniqueness => { :case_sensitive => false }

before_save :generate_auth_token

private

def generate_auth_token
	self.auth_token = SecureRandom.urlsafe_base64
end

end
