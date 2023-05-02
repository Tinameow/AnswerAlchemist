import axios from 'axios';

const baseURL = 'http://127.0.0.1:5000'

const GetQnAList = (keywords=null, limit=100, offset=0) => {
    return new Promise((resolve, reject) => {
      axios
      .get(baseURL+'/search'+'',{
        params: {
          keywords: keywords,
          limit: limit,
          offset: offset
        },
      })
      .then(response => {
        resolve(response.data.data);
      })
      .catch(err => {
        reject(err);
      });
    })
}

const GetQnA = (id) => {
  return new Promise((resolve, reject) => {
    axios
    .get(baseURL+'/question/'+id)
    .then(response => {
      resolve(response.data.data);
    })
    .catch(err => {
      reject(err);
    });
  })
}

export {GetQnAList, GetQnA};