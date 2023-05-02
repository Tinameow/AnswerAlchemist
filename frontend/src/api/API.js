import axios from 'axios';

const baseURL = 'http://127.0.0.1:5000'

const GetQnAList = (keywords=null, ids=null, limit=100, offset=0) => {

    return new Promise((resolve, reject) => {
      axios
      .get(baseURL+'/search'+'',{
        params: {
          keywords: keywords,
          where: ids? {"_id": {"$in": ids}} : null,
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