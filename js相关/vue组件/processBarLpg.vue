<template>
  <div class="process-bar-lpg">
    <label v-if="labelPosition === 'left'" for="">{{ data + '%' }}</label>
    <div class="process-bar-lpg-main">
      <div class="process-bar-lpg-outer">
        <div ref="processBar" class="process-bar-lpg-inner">
          <div v-if="tagSrc" class="process-lpg-tag"><img width="30px" :src="'https://img.alicdn.com/tfs/TB1td1qB5rpK1RjSZFhXXXSdXXa-60-30.png'" /></div>
        </div>
      </div>
    </div>
    <label v-if="labelPosition === 'right'" for="">{{ data + '%' }}</label>
  </div>
</template>

<script>
  export default {
    props: {
      data: { type: Number, default: 50 },
      direction: { type: String, default: 'toRight' },
      labelPosition: { type: String, default: 'right' },
      tagSrc: { type: String, default: '' },
      color: { type: String, default: 'aquamarine' },
      backgroundColor: { type: String, default: 'aliceblue' },
      outlineColor: { type: String, default: 'aliceblue' },
      endRadiuce: { type: Number, default: 0 },
      labelSize: { type: Number, default: 15 },
    },
    data() {
      return {}
    },
    watch: {
      data(a, b) {
        if (a < 100) {
          this.setValue(a)
        } else {
          this.setValue(100)
        }
      },
    },
    mounted() {
      this.setValue(this.data)
      this.$refs.processBar.style.backgroundColor = this.color
      this.$refs.processBar.parentElement.style.backgroundColor = this.backgroundColor
      this.$refs.processBar.parentElement.parentElement.style.borderColor = this.outlineColor
      this.$refs.processBar.parentElement.parentElement.style.fontSize = this.labelSize + 'px'
      document.querySelector('.process-bar-lpg label').style.fontSize = this.labelSize + 'px'
      if (this.direction === 'toLeft') {
        this.$refs.processBar.style.float = 'right'
        this.$refs.processBar.firstChild.style.float = 'left'
        this.$refs.processBar.firstChild.firstChild.style.right = 'unset'
        this.$refs.processBar.firstChild.firstChild.style.left = '-50%'
        this.$refs.processBar.style.borderBottomLeftRadius = this.endRadiuce + 'px'
        this.$refs.processBar.style.borderTopLeftRadius = this.endRadiuce + 'px'
      } else {
        this.$refs.processBar.style.borderBottomRightRadius = this.endRadiuce + 'px'
        this.$refs.processBar.style.borderTopRightRadius = this.endRadiuce + 'px'
      }
    },
    methods: {
      setValue(data) {
        this.$refs.processBar.style.width = data + '%'
      },
    },
  }
</script>

<style lang="scss">
  div.process-bar-lpg {
    div.process-bar-lpg-main {
      position: relative;
      padding: 2px;
      border: solid #00deff 1px;
      width: calc(100% - 4em);
      display: inline-block;
      vertical-align: -webkit-baseline-middle;
      div.process-bar-lpg-outer {
        background-color: aliceblue;
        height: 10px;
        div.process-bar-lpg-inner {
          background-color: aquamarine;
          width: 50%;
          height: 10px;
          div.process-lpg-tag {
            float: right;
            height: 100%;
            width: fit-content;
            img {
              position: relative;
              right: -50%;
              top: -200%;
            }
          }
          // &::before {
          //   content: '';
          //   width: 0;
          //   height: 0;
          //   border: 6px solid transparent;
          //   border-bottom-color: red;
          //   border-right-color: red;
          //   position: absolute;
          //   // left: -10px;
          //   margin-top: -2px;
          //   margin-left: -10px;
          // }
        }
      }
    }

    label {
      color: aliceblue;
      vertical-align: top;
      margin: 0.5em;
    }
  }

  .invert {
    transform: rotateZ(180deg);
  }
</style>
