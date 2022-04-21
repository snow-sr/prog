<script>
import SideNav from "@/components/SideNav.vue";
import ContentArea from "@/components/ContentArea.vue";
import HeaderComponent from "@/components/HeaderComponent.vue";
import FooterComponent from "@/components/FooterComponent.vue";
import BlockComponent from "./components/BlockComponent.vue";

export default {
  components: {
    SideNav,
    ContentArea,
    HeaderComponent,
    FooterComponent,
    Block: BlockComponent,
  },
};
</script>

<template>
  <HeaderComponent></HeaderComponent>
  <ContentArea>
    <Block typeOfBorder="borderBlue">Hey! This is block 1</Block>
    <Block typeOfBorder="borderWhite">Hey! This is block 2</Block>
    <Block typeOfBorder="borderBlue">Hey! This is block 3</Block>
    <Block typeOfBorder="borderBlue">Hey! This is block 4</Block>

    <Block typeOfBorder="borderBlue">Hey! This is block 5</Block>
    <Block typeOfBorder="borderWhite">Hey! This is block 6</Block>
    <Block typeOfBorder="borderBlue">Hey! This is block 7</Block>
    <Block typeOfBorder="borderBlue">Hey! This is block 8</Block>
  </ContentArea>
  <SideNav></SideNav>
  <FooterComponent></FooterComponent>
</template>
