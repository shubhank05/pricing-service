from typing import Dict,List
from models.item import Item
from models.model import Model
from models.user import User
from dataclasses import dataclass, field
import uuid
from common.database import Database
from libs.mailgun import Mailgun
@dataclass(eq=False)
class Alert(Model):
    name: str
    item_id: str
    price_limit: float
    user_email: str
    _id: str = field(default_factory= lambda: uuid.uuid4().hex)
    collection: str = field(init=False, default='alerts')
    def __post_init__(self):
        self.item = Item.get_by_id(self.item_id)
        self.user = User.find_by_email(self.user_email)

    def json(self) -> Dict:
        return{
        "_id": self._id,
        "name": self.name,
        "price_limit":self.price_limit,
        "user_email": self.user_email,
        "item_id": self.item_id
        }

    def load_item_price(self):
        self.item.load_price()
        return self.item.price

    def notify_if_price_reached(self):
        if self.item.price < self.price_limit:
            print(f"Item {self.item} has reched a price under {self.price_limit}, Latest price is: {self.item.price}.")
            print(Mailgun.send_mail(
            [self.user_email],
            f"Notification for {self.name}",
            f"Your alert {self.name} has reached the price under {self.price_limit}. The latest price is {self.item.price}. Go to this url to check the item {self.item.url} ",
            f'<p> Your alert {self.name} has reached the price under {self.price_limit}</p><p>The latest price is {self.item.price}.</p><p>Go to  {self.item.url} to purchase your item.</p>'))
