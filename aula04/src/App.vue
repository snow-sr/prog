<script>
export default {
  data() {
    return {
      theme: true,
    };
  },

  methods: {
    changeTheme: () => {
      if (this.theme == false) {
        let toTurnDark = document.querySelectorAll("#canTurnDark");
        toTurnDark.forEach((element) => {
          element.classList.add("dark");
        });
      }

      let toTurnWhite = document.querySelectorAll("#canTurnDark");
      toTurnWhite.forEach((element) => {
        element.classList.remove("dark");
      });
    },
  },
};
</script>
<template>
  <main id="canTurnDark">
    <div class="header">
      <p class="title">"HAHAHA"</p>
    </div>

    <div class="body" id="canTurnDark">
      <p class="citation">
        "HAHAHAHA HAHAHAHA HAHAHAHA HAHAHAHA HAHAHAHA <br />
        HAHAHAHA HAHAHAHA HAHAHAHA HAHAHAHA HAHAHAHA <br />
        HAHAHAHA HAHAHAHA HAHAHAHA HAHAHAHA HAHAHAHA" <br />
      </p>
    </div>

    <div id="canTurnDark">
      <p class="author" @click="changeTheme()">Joker, The, 2022</p>
    </div>
  </main>
</template>
