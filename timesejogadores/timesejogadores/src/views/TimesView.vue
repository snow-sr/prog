<script></script>

<template>
  <div class="h-screen">
    <div class="m-5 text-center flex flex-col justify-center items-center">
      <label
        for="exampleFormControlInput2"
        class="form-label inline-block mb-2 text-gray-700 text-xl"
        >Gerenciamento de times</label
      >
      <input
        type="text"
        class="form-control block w-full px-4 py-2 w-96 text-xl font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
        id="exampleFormControlInput2"
        placeholder="Insira um time"
      />
      <button
        type="button"
        class="inline-block mt-3 px-6 py-2.5 bg-purple-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-purple-700 hover:shadow-lg focus:bg-purple-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-purple-800 active:shadow-lg transition duration-150 ease-in-out"
      >
        Salvar
      </button>
    </div>

    <div class="list-times">
      <table>
        <thead>
          <tr>
            <td>ID</td>
            <td>Nome</td>
            <td>Ações</td>
          </tr>
        </thead>

        <tbody>
          <tr>
            <td>1</td>
            <td>Time 1</td>
            <td>???</td>
          </tr>
          <tr>
            <td>2</td>
            <td>Time 2</td>
            <td>???</td>
          </tr>
          <tr>
            <td>3</td>
            <td>Time 3</td>
            <td>???</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style>
.title {
  text-align: center;
  margin: 2rem 0;
}

.list-times {
  display: flex;
  justify-content: center;
  margin: 2rem 0;
}

table {
  width: 40%;
  border: 1px solid black;
  border-collapse: collapse;
  text-align: center;
}
table thead {
  background-color: #581c87;
  color: rgb(255, 255, 255);
}
table thead th {
  font-weight: bolder;
}
table tbody tr:nth-child(odd) {
  background-color: #a855f7;
}

table tbody tr:nth-child(even){
  background-color: #e9d5ff;
}
h2 {
  color: black;
}

.container {
  height: 100 rem;
}
</style>
