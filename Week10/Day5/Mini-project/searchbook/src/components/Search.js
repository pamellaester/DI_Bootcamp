import { fromJS } from "immutable";
import _fetch from "isomorphic-fetch";
import fetch from "isomorphic-fetch";
// Constants
// ---------------------------------------
export const SET_BOOKS = "SET_BOOKS";
export const SET_QUERY = "SET_QUERY";
// ---------------------------------------
// Action
// ---------------------------------------
export const setBooks = (books) => {
  return {
    type: SET_BOOKS,
    payload: books,
  };
};

export const setQuery = (query) => {
  return {
    type: SET_QUERY,
    payload: query,
  };
};

export const getBooks = (query) => {
  return (dispatch, getState) => {
    dispatch(setQuery(query));
      _fetch("https://www.googleapis.com/books/v1/volume" + query)
          .then((response) => {
        if (response.status >= 400) {
          throw new Error("Bad response from the server");
        }
        return response.json()   
          }).then(books => {
            dispatch(setBooks(books.items))
          }).catch(error => {
            console.log(error)
        })
  };
};
// ---------------------------------------
// Action handlers
// ---------------------------------------
const ACTION_HANDLERS = {
  [SET_BOOKS]: (state, { payload: books }) => {
    return state.set("books", fromJS(books));
  },
  [SET_QUERY]: (state, { payload: query }) => {
    return state.set("query", fromJS(books));
  },
};
// ---------------------------------------
// Reducer
// ---------------------------------------
const initialState = fromJS({});
export default (state = initialState, action) => {
  const handler = ACTION_HANDLERS(action.type);
  return handler ? handler(state, action) : state;
};
// ---------------------------------------
