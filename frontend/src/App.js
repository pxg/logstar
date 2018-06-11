import React, { Component } from 'react';
import axios from 'axios'
import './App.css';


function CloseButton(props){
  return (
    <div onClick={props.clickClose} className="delete-btn">
      <a className="btn-floating red">
        <i className="large material-icons">clear</i>
      </a>
    </div>
  );
}


function RequestDetail(props) {
  if(props.value === false){
    return null;
  }
  const request = props.value;
  // var content = JSON.stringify(request.response_content, null, 2);
  return (
    <div className="row">
      <div className="col s12">
        <div className="card blue-grey darken-1">
          <div className="card-content white-text">

            <CloseButton clickClose={props.clickClose} />

            <span className="card-title">{ request.url }</span>

            <table>
              <tbody>
                <tr>
                  <th>method</th>
                  <td>{ request.method }</td>
                </tr>
                <tr>
                  <th>status</th>
                  <td>{ request.response_status_code }</td>
                </tr>
                <tr>
                  <th>time</th>
                  <td>{ request.time }</td>
                </tr>
                <tr>
                  <th>created at</th>
                  <td>{ request.created_at }</td>
                </tr>
                <tr>
                  <th>response content</th>
                  <td>{ request.response_content }</td>
                </tr>
                <tr>
                  <th>response headers</th>
                  <td>{ request.response_headers }</td>
                </tr>
              </tbody>
            </table>

        </div>
      </div>
    </div>
  </div>
  );
}


function getStatusCodeDisplay(statusCode) {
    const statusFirstDigit = statusCode.toString()[0];
    if(statusFirstDigit === '4'){
        return statusCode + ' 😢';
    }
    if(statusFirstDigit === '5'){
        return statusCode + ' 😡';
    }
    return statusCode + ' 😀';
}


class App extends Component {

  constructor() {
    super();
    this.state = {
      detailRequest: false,
      aboveId: false,
      belowId: false,
      rows: [],
    }
    this.apiUrl = 'http://127.0.0.1:8000/api/'
    // Research if binding like this is the best technique to use
    this.getOlderItems = this.getOlderItems.bind(this)
    this.addRows = this.addRows.bind(this)
  }

  componentDidMount() {
    this.getItems(this.apiUrl);
    this.timer = setInterval(()=> this.getNewerItems(), 5000);
  }

  componentWillUnmount() {
    this.timer = null;
  }

  getNewerItems() {
    let apiUrl = this.apiUrl;
    if(this.state.aboveId !== false) {
      apiUrl += 'above/' + this.state.aboveId + '/';
    }
    this.getItems(apiUrl);
  }

  getOlderItems() {
    let apiUrl = this.apiUrl;
    if(this.state.belowId !== false){
      apiUrl += 'below/' + this.state.belowId + '/';
    }
    this.getItems(apiUrl);
  }

  getItems(apiUrl) {
    axios.get(apiUrl)
      .then(
        response => this.addRows(response.data)
        // how to call a second function here?
      )
  }

  addRows(data){
    let rows = this.state.rows;
    data.forEach(function(row) {
      rows.push(row);
    });
    rows.sort(function(a, b){
      if(a.id < b.id) return 1;
      if(a.id > b.id) return -1;
      return 0;
    });
    this.setState({rows: rows});
    this.updateApiValues();
  }

  updateApiValues(){
    if(this.state.rows.length > 0) {
      this.setState({aboveId: this.state.rows[0]['id']});
      this.setState({'belowId': this.state.rows[this.state.rows.length - 1]['id']});
    }
  }

  clickRow(request){
    this.setState({'detailRequest': request});
  }

  clickClose(){
    this.setState({'detailRequest': false});
  }

  render() {
    if(this.state.detailRequest) {
      return (
        <RequestDetail
          value={this.state.detailRequest}
          clickClose={() => this.clickClose()}
        />
      );
    }
    return (
      <div>
        <div>
          <table>
            <thead>
              <tr>
                <th>URL</th>
                <th>Time</th>
                <th>Method</th>
                <th>Status</th>
                <th>Created at</th>
              </tr>
            </thead>
            <tbody>
              {this.state.rows.map((r) => (
                <tr key={r.id} onClick={() => this.clickRow(r)}>
                  <td><a target="_launch" href={r.url}>{r.url}</a></td>
                  <td>{r.time}</td>
                  <td>{r.method}</td>
                  <td>{getStatusCodeDisplay(r.response_status_code)}</td>
                  <td>{r.created_at}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <div className='button__container'>
          <a onClick={this.getOlderItems} className="btn-large waves-effect waves-light orange">
            Load More
          </a>
          <p>{this.state.username}</p>
        </div>
      </div>
    );
  }
}

export default App;
