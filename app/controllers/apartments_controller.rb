class ApartmentsController < ApplicationController
  before_filter :signed_in_user, only: [:create, :destroy]
  before_filter :correct_user, only: :destroy

  def create
    @apartment = current_user.apartments.build(params[:apartment])
    if @apartment.save
      flash[:success] = "Apartment created!"
      redirect_to root_url
    else
      @feed_items = []
      render 'static_pages/home'
    end
  end

  def destroy
    @apartment.destroy
    redirect_to root_url
  end

  def apartments
     render 'apartments/apartments'
  end
  private

    def correct_user
      @apartment = current_user.apartments.find_by_id(params[:id])
      redirect_to root_url if @apartment.nil?
    end

end
