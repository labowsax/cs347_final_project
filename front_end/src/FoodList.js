import { useEffect, useState } from "react";
import axios from "axios";

function FoodList() {
  const [foods, setFoods] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/foods/")
      .then(res => setFoods(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h1>Food Items</h1>
      <ul>
        {foods.map(food => (
          <li key={food.id}>
            Id:{food.id}
            Name:{food.foodName} 
            Fat:{food.fat} 
          </li>
        ))}
      </ul>
    </div>
  );
}

export default FoodList;
