import React from 'react'
import classes from "./Result.module.css"
import {
  Table,
  Thead,
  Tbody,
  Tfoot,
  Tr,
  Th,
  Td,
  TableCaption,
  TableContainer,
} from '@chakra-ui/react'
import staticData from "../../static/static.js"
export default function Result() {
  return (
    <div id="res" className='wrapper'>
      <div className={classes.resultBody}>
      <h2>Таблица свежих данных</h2>
      <TableContainer>
        <Table variant='simple'>
          <TableCaption>Все данные в реальном времени</TableCaption>
          <Thead>
            <Tr>
              <Th>Показатель</Th>
              <Th>Значение</Th>
            </Tr>
          </Thead>
          <Tbody>
            {
              staticData?.map((item, index) => (
                <Tr key={index}>
                  <Td>{item}</Td>
                  <Td>Что-то потом</Td>
                </Tr>
              ))
            }
          </Tbody>
          <Tfoot>
            <Tr>
              <Th>Показатель</Th>
              <Th>Значение</Th>
            </Tr>
          </Tfoot>
        </Table>
      </TableContainer>
      </div>
    </div>
  )
}
