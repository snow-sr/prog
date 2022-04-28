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
    <Block typeOfBorder="borderBlue" title="Block 1"></Block>
    <Block typeOfBorder="borderWhite" title="Block 2"></Block>
    <Block typeOfBorder="borderBlue"  title="Block 3"></Block>
    <Block typeOfBorder="borderBlue"  title="Block 4"></Block>
    <Block typeOfBorder="borderBlue"  title="Block 5"></Block>

    <Block typeOfBorder="borderWhite" title="Block 6"></Block>
    <Block typeOfBorder="borderBlue"  title="Block 7"></Block>
    <Block typeOfBorder="borderBlue"  title="Block 8"></Block>
  </ContentArea>
  <SideNav></SideNav>
  <FooterComponent></FooterComponent>
</template>
