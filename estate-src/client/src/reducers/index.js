import {combineReducers} from "redux";
import {propertyListReducer} from "./propertyReducers"

export default combineReducers({
    propertiesList: propertyListReducer,
});