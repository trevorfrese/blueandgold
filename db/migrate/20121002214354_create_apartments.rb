class CreateApartments < ActiveRecord::Migration
  def change
    create_table :apartments do |t|
      t.string :address
      t.string :city
      t.integer :zipcode

      t.timestamps
    end
  end
end
