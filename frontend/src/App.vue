<template>
  <div class="header"><img src="logo.png" width=250>
    <h2>KATALOG ODCZYNNIKÓW</h2>
    <div class="buttons">
      <button>ZALOGUJ SIĘ</button>
      <button @click="showModal=true">KONTAKT</button>
    </div>
  </div>
  <div v-if="showModal">
    <div class="modal-mask">
          <div class="modal-wrapper">
            <div class="modal-container">

              <div class="modal-header">
                <slot name="header">KONTAKT</slot>
              </div>

              <div class="modal-body">
                <slot name="body">Dla zgłoszenia problemu na stronie proszę pisać na istr@umk.pl</slot>
              </div>

              <div class="modal-footer">
                <slot name="footer">
                  <button class="modal-default-button" @click="showModal=false">OK</button>
                </slot>
              </div>
            </div>
          </div>
        </div>
  </div>
  <div class="title">KChMAiK UMK.Pracownia 94-95
    <button class="btn-another-storage">Zmień</button>
  </div>
  <div class="instruction">
    <ul><b>Do wyszukiwania odczynnika można użyć:</b> 
      <li>numer CAS</li>
      <li>angielska lub polska nazwa odczynnika</li>
      <li>wzór sumaryczny (format: Na2CO3 x 10H2O)</li>
    </ul>
    <ul><b>Do wyszukiwania grup odczynników można także użyć słowa kluczowe, np.: Węglany, Ca2+, Wapń, CO32-</b>
    </ul>
  </div>
  <div class="container">
    <input
      type="text"
      class="search"
      v-model="searchText"
      placeholder="Wpisz tu..."
    />
    <span v-if="storage.length"><br><br>Elementów znaleziono: {{ storage.length }}<br><br></span>
    <table v-if="storage.length" class="results">
      <thead>
        <tr>
          <th width="30%">Formuła</th>
          <th width="30%">Nazwa</th>
          <th width="20%">CAS</th>
          <th width="10%">Regał</th>
          <th width="10%">Półka</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(compound, key) in storage" :key="key">
          <td>{{ compound.formula }}</td>
          <td>{{ compound.title || textIfEmpty }}</td>
          <td class="centered-obj">{{ compound.cas || textIfEmpty }}</td>
          <td class="centered-obj">{{ compound.rack }}</td>
          <td class="centered-obj">{{ compound.shelf }}</td>
        </tr>
      </tbody>
    </table>
    <h1 v-else-if="searchText">Nic nie znaleziono</h1>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      storage: [],
      searchText: '',
      textIfEmpty: '-',
      showModal: false,
    }
  },
  watch: {
    searchText() {
      if (this.searchText) {
        this.updateStorageInfo();
      }
      else {
        this.storage = [];
      }
    }
  },
  mounted() {
  },
  methods: {
    updateStorageInfo() {
      fetch('http://127.0.0.1:8000/storage?' + new URLSearchParams({
          search: this.searchText,
        }))
        .then((res) => res.json())
        .then((data) => {
          this.storage = data
        })
    }
  }
}
</script>

<style>
body {
  margin: 0;
  padding: 0;
  font-family: Lato-Regular, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-color: #DCE6Fa;
}

.header {
  display: flex;
  justify-content:space-between;
  
}

.header h2 {
  font-size: 35px;
  text-align: center;
  color: #004492;

  
}

.title {
  text-align: left;
  color: white;
  font-size: 25px;
  padding: 15px;
  margin-top: 10px;  
  border-top: 10px solid #aad23f;
  background-color: #004492;
  letter-spacing: 1.5px;
  display: flex;
  justify-content:space-between;
  
}

.btn-another-storage {
  width: 3cm;
  padding: 5px;
  border-radius: 4px;
}

.btn-another-storage:hover {
  background: #aad23f;
	color: #004492;
  border-radius: 4px;
}


.buttons {
  float: right;
  margin-top: 7px;
  margin: 15px;
}

button {
  padding: 25px;
  font-size: 18px;
  font-family: Lato-Regular, Arial, sans-serif;
  border: 0;
  color: #004492;
  background-color: #DCE6Fa;
}

button:hover {
	background: #004492;
	color: #DCE6Fa;
  border-radius: 2%;
}

.instruction {
  color: #004492;
  padding: 10px;
  font-size: 18px;
  line-height: 30px;
  letter-spacing: 2px;
}

.search {
  color: #004492;
  padding: 10px 5px;
  margin: 5px;
  width: 98%;
  font-size: 1.1em;
}

table {
  border-collapse: collapse;
}

.results {
  color: #004492;
  width: 100%;
  text-align: left;
}

.results th {
  margin: 0;
  border-bottom: 2px solid #004492;
  padding-bottom: 15px;
  text-align: center;
}

.results td {
  margin: 0;
  border-bottom: 1px solid #004492;
  padding: 15px;
}

.centered-obj {
  text-align: center;
}

span {
  color: #004492;
}

h1 {
  color: #004492;
}

.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 500px;
  height: 300px;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #DCE6Fa;
  border-radius: 4px;
  font-family: Lato-Regular, Arial, sans-serif;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.modal-header {
  text-align: center;
  font-size: 40px;
  color: #004492;
  margin-top: 20px;
}

.modal-body {
  margin: 20px 0;
  font-size: 25px;
  color: #004492;

}

.modal-default-button {
  float: right;
  width: 5cm;
  background-color: #aad23f;
}


</style>
