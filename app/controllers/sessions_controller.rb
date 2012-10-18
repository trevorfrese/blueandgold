class SessionsController < ApplicationController
 def new
    @title = "Sign in"
 end
  
 def create
	user = User.find_by_email(params[:email])
	if user && user.authenticate(params[:password])
	cookies[:auth_token] = user.auth_token
	flash[:success] = "Successfully logged in!"
	else if user.nil?
        flash.now[:error] = "Invalid email/password combination."
        @title = "Sign in"
        render 'new'
	end
	redirect_to root_path
end
  
def destroy
#    sign_out
#    cookies.delete(:auth_token)
#    redirect_to root_path
end
end
end
