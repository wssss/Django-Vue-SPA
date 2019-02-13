<template>
      <div class="wrap" v-if="showWrap" :class="showContent ? 'fadein':'fadeout'">
          {{text}}
      </div>
</template>
<script>
export default {
    
}
</script>

<style scoped>
.wrap{
    position: fixed;
    left: 50%;
    top: 50%;
    background: rgba(0, 0, 0, .35);
    padding: 40px;
    border-radius: 5px;
    transform: translate(-50%, -50%);
    color: #ffffff;
}
.fadein{
    animation: animate_in 0.25s;
}
.fadeout{
    animation:animate_out 0.25s;
}
@keyframes animate_in {
    0%{
        opacity: 0;
    }
    100%{
        opacity: 1;
    }
}
@keyframes animate_out {
    0%{
        opacity: 1;
    }
    100%{
        opacity: 0;
    }
}
</style>
