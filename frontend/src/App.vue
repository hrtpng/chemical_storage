<template>
  <div class="container">
    <input
      type="text"
      class="search"
      v-model="searchText"
      placeholder="Wpisz tu..."
    />
    <span v-if="storage.length">Elementów znaleziono: {{ storage.length }}</span>
    <table v-if="storage.length" class="results">
      <thead>
        <tr>
          <th>Formuła</th>
          <th>Nazwa</th>
          <th>CAS</th>
          <th>Regał</th>
          <th>Półka</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="compound in storage" :key="compound.title">
          <td>{{ compound.formula }}</td>
          <td>{{ compound.title || textIfEmpty }}</td>
          <td>{{ compound.cas || textIfEmpty }}</td>
          <td>{{ compound.rack }}</td>
          <td>{{ compound.shelf }}</td>
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
      textIfEmpty: '-'
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
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.search {
  padding: 10px 5px;
  margin: 5px;
  width: 98%;
}
.results {
  width: 100%;
  margin: 10px 5px;
}
.results td {
  text-align: center;
}
</style>
