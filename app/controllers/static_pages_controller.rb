class StaticPagesController < ApplicationController
  def home
     if signed_in?
      @apartment  = current_user.apartments.build
      @feed_items = current_user.feed.paginate(page: params[:page])
    end
  end

  def help
  end

  def contact 
  end

end
