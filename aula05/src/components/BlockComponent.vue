<script>
export default {
  props: {
    title: {
      type: String,
      default: "~sem título~"
    },

    typeOfBorder: {
      type: String,
      default: "",
    },
  },
};
</script>

<template>
  <div :class="[typeOfBorder, 'block']">
    <h1 class="text-lg">{{title}}</h1>
    <hr>
    <slot></slot>
  </div>
</template>
