class AddContentToApartments < ActiveRecord::Migration
  def change
    add_column :apartments, :content, :string
  end
end
